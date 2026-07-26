%define upstream_name    Regexp-Bind
Name:		perl-%{upstream_name}
Version:	0.05
Release:	6

Summary:	Regexp::Bind - Bind variables to captured buffers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Regexp-Bind
Source0:	https://cpan.metacpan.org/authors/id/X/XE/XERN/Regexp-Bind-%{version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module is an extension to perl's native regexp function. It
binds anonymous hashes or named variables to matched buffers. Both
normal regexp syntax and embedded regexp syntax are supported.
You can view it as a tiny and petite data extraction system.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Regexp/Bind.pm
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 404354
- rebuild using %0.05 Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.05-5mdv2009.0
+ Revision: 241849
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 0.05-3mdv2008.0
+ Revision: 25104
- rebuild


* Wed May 03 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-2mdk
- Fix According to perl Policy
	- Source URL
- use mkrel

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdk
- initial Mandriva package

