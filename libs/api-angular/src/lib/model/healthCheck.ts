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
 * Represents the health of a service
 */
export interface HealthCheck {
  /**
   * Indicates whether the service status is acceptable or not
   */
  status: HealthCheck.StatusEnum;
}
export namespace HealthCheck {
  export type StatusEnum = 'pass' | 'fail' | 'warn';
  export const StatusEnum = {
    Pass: 'pass' as StatusEnum,
    Fail: 'fail' as StatusEnum,
    Warn: 'warn' as StatusEnum,
  };
}
