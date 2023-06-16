#!/usr/bin/env python3

# seattle-ops-301d8
# Ops Challenge:Powershell AD Automation
# Demo Code:

#   New-ADUser -Name "ChewDavid" -OtherAttributes @{'title'="director";'mail'="chewdavid@fabrikam.com"}

#ref :https://github.com/adbertram/Random-PowerShell-Work/blob/master/ActiveDirectory/Bulk-AD-User-Creation.ps1
#ref :ChatGPT

# Set the parameters
$firstName = "Franz"
$lastName = "Ferdinand"
$position = "TPS Reporting Lead"
$company = "GlobeX USA"
$office = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"

# Connect to the Active Directory module
Import-Module ActiveDirectory

# Set the user details
$samAccountName = ($firstName.Substring(0,1) + $lastName).ToLower()
$password = "P@ssw0rd"  # Set the initial password for the user

# Create the user
New-ADUser -SamAccountName $samAccountName -GivenName $firstName -Surname $lastName -DisplayName "$lastName, $firstName" `
    -Title $position -Company $company -Office $office -Department $department -EmailAddress $email `
    -UserPrincipalName "$samAccountName@yourdomain.com" -AccountPassword (ConvertTo-SecureString -AsPlainText $password -Force) `
    -Enabled $true -PasswordNeverExpires $true

# Display the created user details
Get-ADUser -Identity $samAccountName
