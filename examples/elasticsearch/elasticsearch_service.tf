# Elasticsearch service
resource "aiven_service" "es" {
  project = aiven_project.es-project.project
  cloud_name = "google-europe-west1"
  plan = "hobbyist"
  service_name = "es-service"
  service_type = "elasticsearch"
  maintenance_window_dow = "monday"
  maintenance_window_time = "10:00:00"
}

# Elasticsearch user
resource "aiven_service_user" "es-user" {
  project = aiven_project.es-project.project
  service_name = aiven_service.es.service_name
  username = "test-user1"
}