%define real_name Regexp-Bind

Summary:	Regexp::Bind - Bind variables to captured buffers
Name:		perl-%{real_name}
Version:	0.05
Release: %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Regexp/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module is an extension to perl's native regexp function. It
binds anonymous hashes or named variables to matched buffers. Both
normal regexp syntax and embedded regexp syntax are supported.
You can view it as a tiny and petite data extraction system.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Regexp/Bind.pm
%{_mandir}/*/*


