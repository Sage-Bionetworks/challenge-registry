import { ModelError as ApiClientError } from '@challenge-registry/api-angular';

// Type guard for ApiClientError
export function isApiClientError(error: any): error is ApiClientError {
  const err = error as ApiClientError;
  return err.status !== undefined && err.title !== undefined;
}
