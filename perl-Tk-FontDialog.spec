#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires working $DISPLAY)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	FontDialog
Summary:	Tk::FontDialog Perl module - font chooser for Perl/Tk
Summary(pl.UTF-8):	Moduł Perla Tk::FontDialog - okienko wyboru fontu dla modułu Perla Tk
Name:		perl-Tk-FontDialog
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	744134636db96c57bcc20299411429ce
BuildRequires:	perl-Tk >= 800
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::FontDialog implements a font dialog widget.

%description -l pl.UTF-8
Moduł Tk::FontDialog jest implementacją okienka wyboru fontu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tk/FontDialog.pm
%{_mandir}/man3/*
