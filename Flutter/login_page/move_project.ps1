# Create the destination directory
$destination = "D:\Projects\login_page"
New-Item -ItemType Directory -Force -Path $destination

# Copy all files and folders except .git and build
Get-ChildItem -Path "." -Exclude @(".git", "build", ".dart_tool", ".idea", ".vscode") | 
Copy-Item -Destination $destination -Recurse -Force

Write-Host "Project files have been copied to $destination"
Write-Host "Please navigate to the new location and run:"
Write-Host "flutter clean"
Write-Host "flutter pub get"
Write-Host "flutter run" 