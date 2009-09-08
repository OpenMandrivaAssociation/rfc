%define name    rfc
%define version 3.2
%define release %mkrel 5

Summary:       Simple scripts for downloading and reading RFCs
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{name}-%{version}.tar.bz2
License:       Public Domain
Group:         Networking/Other
BuildRoot:     %{_tmppath}/%{name}-buildroot
Url:           http://www.dewn.com/rfc/
Requires:      lynx
BuildArch:     noarch

%description
This package contains a script for reading RFCs off the Internet
from the shell (by starting your favorite browser, or just dumping
it to stdout). It also includes an emacs list package to read RFCs 
from emacs.

%prep
%setup -q

%build
sed -i "s/# potential browsers, order of perference/my \$dumper=qw(lynx);/" %{name}-%{version}
sed -i "s/viewer -dump/dumper -dump/" %{name}-%{version}
sed -i "s/w3m lynx/\$TEXTBROWSER links lynx w3m \$BROWSER/" %{name}-%{version}
sed -i 's$/usr/local/etc$/var/cache/rfc$' %{name}-%{version}
sed -i 's$/local/path/to/rfcs$/var/cache/rfc$' %{name}-%{version}
sed -i 's$/ftp.isi.edu/in-notes/iana$/www.iana.org$' %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/var/cache/rfc/
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/emacs/site-lisp/
ln -s %{name}-%{version} %{name}
install -m755 %{name}-%{version} $RPM_BUILD_ROOT/%{_bindir}/
install -m755 %{name} $RPM_BUILD_ROOT/%{_bindir}/
install -m644 rfc-util.el $RPM_BUILD_ROOT/%{_datadir}/emacs/site-lisp/

%post
%{_bindir}/%{name} -i
%{_bindir}/%{name} -n -i

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}-%{version}
%{_bindir}/%{name}
%{_datadir}/emacs/site-lisp/rfc-util.el
%dir /var/cache/rfc

