%global debug_package %{nil}

Name:           neofetch
Version:        6.0.0
Release:        1%{?dist}
Summary:        CLI system information tool written in Bash
License:        MIT
URL:            https://github.com/dylanaraps/%{name}
BuildArch:      noarch
Requires:       bash >= 3.0


%description
Neofetch displays information about your system next to an image,
your OS logo, or any ASCII file of your choice. The main purpose of Neofetch
is to be used in screenshots to show other users what OS/distribution you're
running, what theme/icons you're using and more.


%prep
wget https://github.com/dylanaraps/%{name}/archive/%{version}.tar.gz
tar xzf %{version}.tar.gz


%build
cd %{name}-%{version}
sed 's,/usr/bin/env bash,/bin/bash,g' -i neofetch


%install
cd %{name}-%{version}
%make_install

%files
%{_bindir}/%{name}
%doc %{name}-%{version}/README.md %{name}-%{version}/CHANGELOG.md
%{_mandir}/man1/%{name}.1*


%changelog
* Wed Jan 9 2019 Jamie Curnow <jc@jc21.com> - 6.0.0-1
- v6.0.0

* Mon Jul 9 2018 Jamie Curnow <jc@jc21.com> - 5.0.0-1
- Initial package.

