# Case II - GitHub Actions

  Create a Python API / Java / dotNet / Javascript Project (Select one)
  Make a GitHub Workflow appear on GitHub Actions by creating a workflow in the repository.
  When a change detected on the GitHub Repository, GitHub Actions must be auto-triggered and run the pipeline
  Define the following operations on GitHub Wokflow.

## Operations (Stages):
  1. Code Build
  2. Code Test (ignore the error status if it gives an error.)
  3. Code Analyze (SonarQube)
  4. Dockerize
  5. Push Image to DockerHub
  6. Container Scaning (Clair or Trivy) 
