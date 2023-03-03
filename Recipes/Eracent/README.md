# Eracent AutoPkg Recipes

The recipes in this folder help automate the process of downloading the latest version of the Eracent clients installation package for macOS and modifying it to install smoothly with Microsoft Intune.

## Preqrequisites

To use these recipes, you must meet the following requirements:

1. Running macOS 10.6 or later.
2. [Git](https://git-scm.com/) is installed.
3. [AutoPkg](https://github.com/autopkg/autopkg/wiki/Getting-Started) is installed.
4. This repo is added to your recipe sources: `autopkg repo-add https://github.com/microsoft/intune-autopkg-recipes`.

Additionally, you must have a valid Apple [*Developer ID Installer*](https://developer.apple.com/help/account/create-certificates/create-developer-id-certificates/) certificate for signing PKGs.

## Instructions

### Step 1: Run the Recipe

There are two ways to run this recipe depending on where your installer package lives.

#### Option 1: Using a Download URL

If your installer package is hosted on an internal website, run the recipe with the following arguments:

```zsh
autopkg run com.github.Microsoft.intune.Eracent --key DOWNLOAD_URL="https://yourwebsite.com/path/to/eracent.pkg" --key SIGNING_CERT="<cert common name>"
```

Replace the values for `DOWNLOAD_URL` and `SIGNING_CERT` with the full URL to download the PKG and the common name for your developer ID installer certificate respectively. Replace the values for `HOSTNAME` and `SIGNING_CERT` with the hostname for your PaloAlto VPN gateway and the common name for developer ID installer certificate respectively. The common name for your certificate should look something like `Developer ID Installer: Your Company (XXXXXXXXXX)`.

#### Option 2: Using a Local Copy

Alternatively, you can run the recipe against a local copy of the PKG:

```zsh
autopkg run com.github.Microsoft.intune.Eracent --key LOCAL_PKG="/path/to/your/local/eracent.pkg" --key SIGNING_CERT="<cert common name>"
```

Replace the values for `LOCAL_PKG` and `SIGNING_CERT` with the local path to your PKG and the common name for your developer ID installer certificate respectively. Replace the values for `HOSTNAME` and `SIGNING_CERT` with the hostname for your PaloAlto VPN gateway and the common name for developer ID installer certificate respectively. The common name for your certificate should look something like `Developer ID Installer: Your Company (XXXXXXXXXX)`.

### Step 2: Validate the Output

After running the command, you should see a `MACOSX_intel_ClientsInstaller_1_EPA_EPM_EDA-intune.pkg` file in your current working directory, which you can use to distribute using Microsoft Intune. You can verify that the file was signed correctly using an app such as [Suspicious Package](https://mothersruin.com/software/SuspiciousPackage/) or by running the command `pkgutil --check-signature ./MACOSX_intel_ClientsInstaller_1_EPA_EPM_EDA-intune.pkg`.

### Step 3: Upload to Microsoft Intune

Upload the application to the Intune admin portal following the steps outlined [here](https://learn.microsoft.com/en-us/mem/intune/apps/lob-apps-macos).

Replace the bundle IDs listed in the bundle ID table with the following values:
- `EracentEPMService-Darwin`
- `EracentEDAService-Darwin`
- `EracentEPMClient-Darwin`
- `EracentEPAService-Darwin`

For the app version fields, use the same version that was automatically detected when uploading the app for all four bundle IDs.