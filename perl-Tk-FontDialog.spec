%include	/usr/lib/rpm/macros.perl
%define		pdir	Tk
%define		pnam	FontDialog
Summary:	Tk::FontDialog Perl module - font chooser for Perl/Tk
Summary(pl):	Modu³ Perla Tk::FontDialog - okienko wyboru fontu dla modu³u Tk
Name:		perl-Tk-FontDialog
Version:	0.08
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tk >= 800
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tk::FontDialog implements a font dialog widget.

%description -l pl
Modu³ Tk::FontDialog jest implementacj± okienka wyboru fontu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Tk/FontDialog.pm
%{_mandir}/man3/*
