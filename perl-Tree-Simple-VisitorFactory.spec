%define upstream_name    Tree-Simple-VisitorFactory
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A Visitor for sorting a Tree::Simple object hierarchy
License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tree/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Tree::Simple)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Tree
%{_mandir}/*/*

%clean
rm -rf %{buildroot}
