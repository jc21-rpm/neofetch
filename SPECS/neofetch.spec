%global debug_package %{nil}

Name:           neofetch
Version:        7.0.0
Release:        1%{?dist}
Summary:        CLI system information tool written in Bash
License:        MIT
URL:            https://github.com/dylanaraps/%{name}
Source:         https://github.com/dylanaraps/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
Requires:       bash >= 3.0


%description
Neofetch displays information about your system next to an image,
your OS logo, or any ASCII file of your choice. The main purpose of Neofetch
is to be used in screenshots to show other users what OS/distribution you're
running, what theme/icons you're using and more.


%prep
%setup -n %{name}-%{version}

%build
sed 's,/usr/bin/env bash,/bin/bash,g' -i neofetch

%install
%make_install

%files
%{_bindir}/%{name}
%doc README.md LICENSE.md
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Mar 9 2020 Jamie Curnow <jc@jc21.com> - 7.0.0-1
- v7.0.0

* Wed Jan 9 2019 Jamie Curnow <jc@jc21.com> - 6.0.0-1
- v6.0.0

* Mon Jul 9 2018 Jamie Curnow <jc@jc21.com> - 5.0.0-1
- Initial package.

