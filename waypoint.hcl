project = "flask-example"

app "flask-example_app {
  labels = {
    "service" = "flask-example_app",
    "env" = "dev"
  }

  build {
    use "docker" {}
  }

  deploy { 
    use "docker" {
        service_port = 8000
    }
  }
}
