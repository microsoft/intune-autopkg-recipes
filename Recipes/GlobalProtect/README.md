# GlobalProtect AutoPkg Recipes

The recipes in this folder help automate the process of downloading the latest version of the GlobalProtect installation package for macOS and modifying it to install smoothly with Microsoft Intune.

## Preqrequisites

To use these recipes, you must meet the following requirements:

1. Running macOS 10.6 or later.
2. [Git](https://git-scm.com/) is installed.
3. [AutoPkg](https://github.com/autopkg/autopkg/wiki/Getting-Started) is installed.
4. This repo is added to your recipe sources: `autopkg repo-add https://github.com/microsoft/intune-autopkg-recipes`.

Additionally, you must have a valid Apple [*Developer ID Installer*](https://developer.apple.com/help/account/create-certificates/create-developer-id-certificates/) certificate for signing PKGs.

## Instructions

### Step 1: Run the Recipe

Run the following command in Terminal:

```zsh
autopkg run com.github.Microsoft.intune.GlobalProtect --key HOSTNAME="<yourvpngateway.com>" --key SIGNING_CERT="<cert common name>"
```

Replace the values for `HOSTNAME` and `SIGNING_CERT` with the hostname for your PaloAlto VPN gateway and the common name for developer ID installer certificate respectively. The common name for your certificate should look something like `Developer ID Installer: Your Company (XXXXXXXXXX)`.

### Step 2: Validate the Output

After running the command, you should see a `GlobalProtectIntune.pkg` file in your current working directory, which you can use to distribute using Microsoft Intune. You can verify that the file was signed correctly using an app such as [Suspicious Package](https://mothersruin.com/software/SuspiciousPackage/) or by running the command `pkgutil --check-signature ./GlobalProtectIntune.pkg`.

### Step 3: Upload to Microsoft Intune

Upload the application to the Intune admin portal following the steps outlined [here](https://learn.microsoft.com/en-us/mem/intune/apps/lob-apps-macos). In the app bundle ID table, make sure only `com.paloaltonetworks.GlobalProtect.client` is listed. Remove any extraneous bundle IDs.