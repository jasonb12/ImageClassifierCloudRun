import subprocess
import os

def install_gcloud_cli():
  """Installs the gcloud CLI on creation of a Codespaces environment."""

  # Check if the gcloud CLI is already installed.
  if "gcloud" in os.listdir("/usr/local/bin"):
    return

  # Install the gcloud CLI.
  if not os.path.isfile("google-cloud-cli-431.0.0-linux-x86_64.tar.gz"):
    subprocess.run(["curl", "-O", "https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-431.0.0-linux-x86_64.tar.gz"], check=True)

  # Extract the installer.
  subprocess.run(["tar", "-xf", "google-cloud-cli-431.0.0-linux-x86_64.tar.gz"], check=True)

  # Install the SDK.
  subprocess.run(["./google-cloud-sdk/install.sh","-q"], check=True)

  # Add the gcloud CLI to the PATH.
  os.environ["PATH"] += ":" + os.path.join("/workspaces/ImageClassifierCloudRun/.devcontainer/google-cloud-sdk/bin")

  # Check if the gcloud CLI is installed correctly.
  try:
    subprocess.run(["gcloud", "--version"], check=True)
  except subprocess.CalledProcessError:
    raise RuntimeError("Failed to install gcloud CLI")

if __name__ == "__main__":
  install_gcloud_cli()
