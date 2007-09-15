%define module Tree-Simple-VisitorFactory
%define name perl-%{module}
%define version 0.10
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A Visitor for sorting a Tree::Simple object hierarchy
License:        Artistic/GPL
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Tree/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Tree::Simple)
BuildArch:      noarch
Buildroot:      %{_tmppath}/%{name}-%{version}

%description
This implements a recursive multi-level sort of a Tree::Simple hierarchy.

%prep
%setup -q -n %{module}-%{version}

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

