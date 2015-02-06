%define major 1
%define libname %mklibname ppd %{major}
%define devname %mklibname ppd -d

Summary:	Library for handling PPD (PostScript Printer Description) files
Name:		libppd
Version:	0.10
Release:	17
License:	GPLv2+
Group:		Publishing
Url:		http://sourceforge.net/projects/lpr/
Source0:	http://sourceforge.net/projects/lpr/libppd-0.10.tar.bz2
Patch0:		libppd-0.10-autotools.patch
BuildRequires:	pkgconfig(glib)

%description
libppd is a library for handling PPD (PostScript Printer Description)
files, its functions parse the files, list printer options and choices
described in the files to set up GUIs for printing, and it inserts
PostScript commands into PostScript files so that the option settings
of the user are applied to the PostScript print job.

#----------------------------------------------------------------------------

%package -n ppdfilt
Summary:	Sets options according to a PPD file in a PostScript file
Group:		Publishing

%description -n ppdfilt
ppdfilt is a filter which takes PostScript as input, inserts
PostScripy code according to a PPD file and user-supplied option
settings, and puts out the result. Sending a so prepared PostScript
file to the printer to which the PPD file belongs, the printer does
the job with the options as set by the user.

%files -n ppdfilt
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/postscript

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for handling PPD (PostScript Printer Description) files
Group:		Publishing

%description -n %{libname}
libppd is a library for handling PPD (PostScript Printer Description)
files, its functions parse the files, list printer options and choices
described in the files to set up GUIs for printing, and it inserts
PostScript commands into PostScript files so that the option settings
of the user are applied to the PostScript print job.

%files -n %{libname}
%{_libdir}/libppd.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers and links to compile against the "%{libname}" library
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains all files which one needs to compile programs using
the "%{libname}" library.

%files -n %{devname}
%doc AUTHORS ChangeLog TODO
%{_includedir}/*.h
%{_libdir}/*.so
%{_mandir}/man3/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .automake

%build
autoreconf -fi
%configure2_5x --disable-static
# Parallel build is not safe: tested by AdamW 2007/07
make

%install
%makeinstall_std

