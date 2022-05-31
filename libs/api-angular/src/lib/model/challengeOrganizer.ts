/**
 * Registry of Open Community Challenges API
 * The OpenAPI specification implemented by the Challenge Registries. # Introduction TBA
 *
 * The version of the OpenAPI document: 0.6.0
 * Contact: thomas.schaffter@sagebionetworks.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { ChallengeOrganizerRole } from './challengeOrganizerRole';
import { ChallengeOrganizerCreateRequest } from './challengeOrganizerCreateRequest';
import { ChallengeOrganizerCreateResponse } from './challengeOrganizerCreateResponse';

/**
 * A challenge organizer
 */
export interface ChallengeOrganizer {
  /**
   * The unique identifier of a challenge organizer
   */
  id: string;
  name: string;
  /**
   * The user or organization account name
   */
  login?: string;
  roles?: Array<ChallengeOrganizerRole>;
}
