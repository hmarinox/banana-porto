project = "flask-example"

app "flask-example_app" {
  labels = {
    "service" = "flask-example",
    "env" = "dev"
  }

  build {
    use "docker" {}
  }

  deploy { 
    use "docker" {
       # command = ["./compose.sh"]
        client_config {
          host = "ssh://ubuntu@192.168.64.11"
        }
    }
  }
}

