%define upstream_name    Dist-Zilla-Plugin-MetaProvides-Class
%define upstream_version 1.11034201

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Scans files and tries to identify classes using Class::Discover
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Discover)
BuildRequires:	perl(Dist::Zilla::App::Tester)
BuildRequires:	perl(Dist::Zilla::MetaProvides::ProvideRecord)
BuildRequires:	perl(Dist::Zilla::Plugin::MetaProvides)
BuildRequires:	perl(Dist::Zilla::Role::MetaProvider::Provider)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(MooseX::Declare)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Module::Build)
BuildArch:	noarch

%description
Scans files and tries to identify classes using Class::Discover.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
#/Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

