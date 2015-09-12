Name:           b43-firmware-install
Summary:        Package that installs proprietary firmware for Broadcom 43xx chips
Version:        0.1
Release:        4
Source:         %name-%version.tar.bz2
License:        GPLv3
Group:          System/Configuration/Networking
URL:            https://github.com/mikhirev/b43-firmware-install
BuildArch:      noarch
Requires:       b43-fwcutter >= 015

%description
This package contains script, that automatically downloads precompiled
proprietary broadcom-wl driver and extracts firmware from it using
b43-fwcutter.

There are no any proprietary components in package itself. Driver will be
downloaded after ihnstallation, so you need working Internet connection. You
can also install firmware later by running b43-firmware-install as root.


%prep
%setup -q

%build

%install
install -D -m 755 b43-firmware-install %{buildroot}/usr/sbin/b43-firmware-install

%post
/usr/sbin/b43-firmware-install

%postun
rm -rf /lib/firmware/b43

%files
%defattr(-,root,root)
/usr/sbin/b43-firmware-install
%doc README
