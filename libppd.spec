%define major		1
%define libname		%mklibname ppd %{major}
%define develname	%mklibname ppd -d

Summary:	Library for handling PPD (PostScript Printer Description) files
Name:		libppd
Version:	0.10
Release:	15
License:	GPLv2
Group:		Publishing
Source:		http://sourceforge.net/projects/lpr/libppd-0.10.tar.bz2
Patch0:		libppd-0.10-autotools.patch
Url:		http://sourceforge.net/projects/lpr/
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
%patch0 -p1 -b .automake

%build
autoreconf -fi
%configure2_5x
# Parallel build is not safe: tested by AdamW 2007/07
make

%install
%makeinstall

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
%{_mandir}/man3/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10-14mdv2011.0
+ Revision: 620215
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.10-13mdv2010.0
+ Revision: 429827
- rebuild

  + Arnaud Patard <apatard@mandriva.com>
    - Fix build fix newer libtool (remove old libtool patch, fix src/Makefile.am)

  + Funda Wang <fwang@mandriva.org>
    - use configure2_5x

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.10-11mdv2009.0
+ Revision: 222967
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.10-10mdv2008.1
+ Revision: 178991
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 01 2007 Adam Williamson <awilliamson@mandriva.org> 0.10-8mdv2008.0
+ Revision: 57305
- no need to package COPYING or INSTALL
- add comment on parallel build not working
- rebuild for 2008
- move docs to -devel package
- don't do the doc installation manually, just use the macro
- new devel policy
- buildrequires autoconf
- clarify license as GPLv2
- bunzip2 patch
- spec clean
- Import libppd



* Tue Jul 11 2006 Till Kamppeter <till@mandriva.com> 0.10-7mdv2007.0
- Rebuilt

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.10-7mdk
- Rebuild

* Sun Aug 14 2005 Till Kamppeter <till@mandriva.com> 0.10-6mdk
- Rebuilt to remove the dust of 12 months.

* Sun Jul 25 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.10-5mdk
- libtool fixes

* Wed Sep 17 2003 Till Kamppeter <till@mandrakesoft.com> 0.10-4mdk
- Renamed source RPM and specfile to not contain major.
- Corrected group of libppd-devel.
- rpmlint fixes.

* Tue Sep  2 2003 Till Kamppeter <till@mandrakesoft.com> 0.10-3mdk
- Used the mklibname macro.

* Sat Jul 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.10-2mdk
- rebuild
- clean out stuff

* Thu Jan 10 2001 Till Kamppeter <till@mandrakesoft.com> 0.10-1mdk
- New version.

* Thu Jan 10 2001 Till Kamppeter <till@mandrakesoft.com> 0.9-1mdk
- Initial release.
