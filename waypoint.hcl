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
    use "exec" {
        command = ["./compose.sh"]

    }
  }
}

