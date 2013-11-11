%define upstream_name    Tree-Simple-VisitorFactory
%define upstream_version 0.12

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    1

Summary:    A Visitor for sorting a Tree::Simple object hierarchy
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tree/Tree-Simple-VisitorFactory-%{upstream_version}.tgz

BuildRequires:  perl-devel
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Tree::Simple)
BuildArch:      noarch

%description
This implements a recursive multi-level sort of a Tree::Simple hierarchy.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Tree
%{_mandir}/*/*

%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 405769
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-7mdv2009.0
+ Revision: 258707
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.10-6mdv2009.0
+ Revision: 246666
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.10-4mdv2008.1
+ Revision: 136364
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-4mdv2008.0
+ Revision: 87063
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-3mdv2007.0
- Rebuild

* Mon Apr 03 2006 Buchan Milne <bgmilne@mandriva.org> 0.10-2mdk
- Rebuild
- use mkrel

* Wed Dec 14 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdk
- New release 0.10

* Wed Sep 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.07-1mdk
- new version 
- rpmbuildupdate aware
- fix directory ownership
- make test in %%check

* Tue May 03 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.05-1mdk
- First Mandriva release


