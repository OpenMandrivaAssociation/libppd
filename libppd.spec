%define name	libppd
%define version	0.10

%define major		1
%define libname		%mklibname ppd %{major}
%define develname	%mklibname ppd -d

Summary:	Library for handling PPD (PostScript Printer Description) files
Name:		%{name}
Version:	%{version}
Release:	%mkrel 11
License:	GPLv2
Group:		Publishing
Source:		http://sourceforge.net/projects/lpr/libppd-0.10.tar.bz2
Patch0:		libppd-0.10-libtool.patch
Url:		http://sourceforge.net/projects/lpr/
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libglib-devel
BuildRequires:	autoconf

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


%package -n %{develname}
Summary: Headers and links to compile against the "%{libname}" library
Requires: 	%{libname} >= %{version}
Provides:	libppd-devel
Obsoletes:	%{mklibname ppd 1 -d}
Group:		Development/C

%description -n %{develname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%prep
%setup -q
%patch0 -p1 -b .libtool
autoconf
find . -name Makefile.in | xargs touch

%build

%configure
# Parallel build is not safe: tested by AdamW 2007/07
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

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

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog TODO
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_mandir}/man3/*
