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
import { GrantCreateResponse } from './grantCreateResponse';
import { GrantCreateRequest } from './grantCreateRequest';

/**
 * Information about monetary resources for challenge
 */
export interface Grant {
  /**
   * The unique identifier of a grant
   */
  id: string;
  /**
   * The name of the grant
   */
  name: string;
}
