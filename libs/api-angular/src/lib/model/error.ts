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

/**
 * Problem details (tools.ietf.org/html/rfc7807)
 */
export interface ModelError {
  /**
   * A human readable documentation for the problem type
   */
  title: string;
  /**
   * The HTTP status code
   */
  status: number;
  /**
   * A human readable explanation specific to this occurrence of the problem
   */
  detail?: string;
  /**
   * An absolute URI that identifies the problem type
   */
  type?: string;
}
