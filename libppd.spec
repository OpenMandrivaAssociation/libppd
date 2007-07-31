
%define major	1
%define libname	%mklibname ppd %{major}

Summary:	Library for handling PPD (PostScript Printer Description) files
Name:		libppd
Version:	0.10
Release:	%mkrel 7
License:	GPL
Group:		Publishing
Source:		http://sourceforge.net/projects/lpr/libppd-0.10.tar.bz2
Patch0:		libppd-0.10-libtool.patch.bz2
Url:		http://sourceforge.net/projects/lpr/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libglib-devel

%description
libppd is a library for handling PPD (PostScript Printer Description)
files, its functions parse the files, list printer options and choices
described in the files to set up GUIs for printing, and it inserts
PostScript commands into PostScript files so that the option settings
of the user are applied to the PostScript print job.

%package -n %{libname}
Summary:	Library for handling PPD (PostScript Printer Description) files
Provides:	libppd
Group:		Publishing

%description -n %{libname}
libppd is a library for handling PPD (PostScript Printer Description)
files, its functions parse the files, list printer options and choices
described in the files to set up GUIs for printing, and it inserts
PostScript commands into PostScript files so that the option settings
of the user are applied to the PostScript print job.

%package -n ppdfilt
Summary: Sets options according to a PPD file in a PostScript file
Group:		Publishing

%description -n ppdfilt
ppdfilt is a filter which takes PostScript as input, inserts
PostScripy code according to a PPD file and user-supplied option
settings, and puts out the result. Sending a so prepared PostScript
file to the printer to which the PPD file belongs, the printer does
the job with the options as set by the user.


%package -n %{libname}-devel
Summary: Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} >= %{version}
Provides:	libppd-devel
Group:		Development/C

%description -n %{libname}-devel
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q -n libppd-%{version}
%patch0 -p1 -b .libtool
autoconf
find . -name Makefile.in | xargs touch

%build

%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# Install doc files
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{libname}-%{version}/
cp AUTHORS COPYING ChangeLog INSTALL TODO $RPM_BUILD_ROOT%{_docdir}/%{libname}-%{version}/

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT


%files -n ppdfilt
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/postscript

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%docdir %{_docdir}/libppd-%{version}
%{_docdir}/%{libname}-%{version}

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*
