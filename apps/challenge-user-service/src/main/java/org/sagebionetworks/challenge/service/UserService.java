package org.sagebionetworks.challenge.service;

import org.sagebionetworks.challenge.model.dto.UserStatus;
import org.sagebionetworks.challenge.exception.GlobalErrorCode;
import org.sagebionetworks.challenge.exception.InvalidChallengeUserException;
import org.sagebionetworks.challenge.exception.InvalidEmailException;
import org.sagebionetworks.challenge.exception.UserAlreadyRegisteredException;
import org.sagebionetworks.challenge.model.dto.User;
import org.sagebionetworks.challenge.model.dto.UserUpdateRequest;
import org.sagebionetworks.challenge.model.entity.UserEntity;
import org.sagebionetworks.challenge.model.mapper.UserMapper;
import org.sagebionetworks.challenge.model.repository.UserRepository;
import org.sagebionetworks.challenge.model.rest.response.UserResponse;
import org.sagebionetworks.challenge.service.rest.ChallengeCoreRestClient;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.keycloak.representations.idm.CredentialRepresentation;
import org.keycloak.representations.idm.UserRepresentation;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import javax.persistence.EntityNotFoundException;
import java.util.Collections;
import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class UserService {
  private final KeycloakUserService keycloakUserService;
  private final UserRepository userRepository;

  private UserMapper userMapper = new UserMapper();

  public User createUser(User user) {
    List<UserRepresentation> userRepresentations =
        keycloakUserService.readUserByEmail(user.getEmail());
    if (userRepresentations.size() > 0) {
      throw new UserAlreadyRegisteredException(
          "This email already registered as a user. Please check and retry.",
          GlobalErrorCode.ERROR_EMAIL_REGISTERED);
    }

    UserRepresentation userRepresentation = new UserRepresentation();
    userRepresentation.setEmail(user.getEmail());
    userRepresentation.setEmailVerified(false);
    userRepresentation.setEnabled(false);
    userRepresentation.setUsername(user.getEmail());

    CredentialRepresentation credentialRepresentation = new CredentialRepresentation();
    credentialRepresentation.setValue(user.getPassword());
    credentialRepresentation.setTemporary(false);
    userRepresentation.setCredentials(Collections.singletonList(credentialRepresentation));

    Integer userCreationResponse = keycloakUserService.createUser(userRepresentation);

    if (userCreationResponse == 201) {
      log.info("User created under given username {}", user.getEmail());

      List<UserRepresentation> userRepresentations1 =
          keycloakUserService.readUserByEmail(user.getEmail());
      user.setAuthId(userRepresentations1.get(0).getId());
      user.setStatus(UserStatus.PENDING);
      UserEntity userEntity = userRepository.save(userMapper.convertToEntity(user));
      return userMapper.convertToDto(userEntity);
    }

    throw new InvalidChallengeUserException("Unable to create the new user",
        GlobalErrorCode.ERROR_INVALID_USER);
  }

  public List<User> readUsers(Pageable pageable) {
    Page<UserEntity> allUsersInDb = userRepository.findAll(pageable);
    List<User> users = userMapper.convertToDtoList(allUsersInDb.getContent());
    users.forEach(user -> {
      UserRepresentation userRepresentation = keycloakUserService.readUser(user.getAuthId());
      user.setId(user.getId());
      user.setEmail(userRepresentation.getEmail());
    });
    return users;
  }

  public User readUser(Long userId) {
    return userMapper
        .convertToDto(userRepository.findById(userId).orElseThrow(EntityNotFoundException::new));
  }

  public User updateUser(Long id, UserUpdateRequest userUpdateRequest) {
    UserEntity userEntity = userRepository.findById(id).orElseThrow(EntityNotFoundException::new);

    if (userUpdateRequest.getStatus() == UserStatus.APPROVED) {
      UserRepresentation userRepresentation = keycloakUserService.readUser(userEntity.getAuthId());
      userRepresentation.setEnabled(true);
      userRepresentation.setEmailVerified(true);
      keycloakUserService.updateUser(userRepresentation);
    }

    userEntity.setStatus(userUpdateRequest.getStatus());
    return userMapper.convertToDto(userRepository.save(userEntity));
  }

}
