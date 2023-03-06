# Zscaler AutoPkg Recipes

The recipes in this folder help automate the process of downloading Zscaler client's installation package for macOS and modifying it to install smoothly with Microsoft Intune. Please keep in mind, this process signs the package; *using a Zscaler version 3.9 or later should not require this.*

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
autopkg run com.github.Microsoft.intune.Zscaler --key DOWNLOAD_URL="https://yourwebsite.com/path/to/Zscaler.pkg" --key SIGNING_CERT="<cert common name>"
```

Replace the values for `DOWNLOAD_URL` and `SIGNING_CERT` with the full URL to download the PKG and the common name for your developer ID installer certificate respectively. The common name for your certificate should look something like `Developer ID Installer: Your Company (XXXXXXXXXX)`.

Note: if you are getting the latest version, you can likely upload directly to Intune, verify that the bundle ID is correct, and skip the rest of this document.

#### Option 2: Using a Local Copy

Alternatively, you can run the recipe against a local copy of the PKG:

```zsh
autopkg run com.github.Microsoft.intune.Zscaler --key LOCAL_PKG="/path/to/your/local/eracent.pkg" --key SIGNING_CERT="<cert common name>"
```

Replace the values for `PKG_PATH` and `SIGNING_CERT` with the local path to your PKG and the common name for your developer ID installer certificate respectively. The common name for your certificate should look something like `Developer ID Installer: Your Company (XXXXXXXXXX)`.

### Step 2: Validate the Output

After running the command, you should see a `Zscaler-osx-3.2.5.5-installer.pkg` file in your current working directory, which you can use to distribute using Microsoft Intune. You can verify that the file was signed correctly using an app such as [Suspicious Package](https://mothersruin.com/software/SuspiciousPackage/) or by running the command `pkgutil --check-signature ./MZscaler-osx-3.2.5.5-installer.pkg`.

### Step 3: Upload to Microsoft Intune

Upload the application to the Intune admin portal following the steps outlined [here](https://learn.microsoft.com/en-us/mem/intune/apps/lob-apps-macos).

Set `Publisher` to `Zscaler, inc`.

Set `Ignore app version` to `true`.

Replace the bundle IDs listed in the bundle ID table with the following values:
- `com.zscaler.Zscaler`

For the app version fields, use the same version that was automatically detected when uploading the app for all four bundle IDs.