# Identify the target USB drive (ensure correct drive letter)
$usbDrive = "D:"

# Format the USB drive
#Format-Volume -DriveLetter D -FileSystem NTFS  -NewFileSystemLabel "Debian" -Confirm:$false

# Mount the ISO file
$isoPath = "C:\testing\debian-12.9.0-amd64-netinst.iso"
$mountResult = Mount-DiskImage -ImagePath $isoPath -PassThru
$volumeInfo = $mountResult | Get-Volume

# Copy files to the USB
$isoDriveLetter = $volumeInfo.DriveLetter
xcopy "$($isoDriveLetter):\*" "$usbDrive\" /s /e

# Clean up: Unmount the ISO
Dismount-DiskImage -ImagePath $isoPath