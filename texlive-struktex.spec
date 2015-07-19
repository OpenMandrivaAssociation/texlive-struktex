# revision 25916
# category Package
# catalog-ctan /macros/latex/contrib/struktex
# catalog-date 2012-04-11 11:11:10 +0200
# catalog-license lppl1.2
# catalog-version 141
Name:		texlive-struktex
Version:	141
Release:	9
Summary:	Draw Nassi-Schneidermann charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/struktex
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Even in the age of OOP one must develop algorithms. Nassi-
Shneiderman diagrams are a well known tool to describe an
algorithm in a graphical way. The package offers some macros
for generating those diagrams in a LaTeX document. The package
provides the most important elements of a Nassi-Shneiderman
diagram, including processing blocks, loops, mapping
conventions for alternatives, etc. Diagrams are drawn using the
picture environment (using pict2e for preference).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/struktex/strukdoc.sty
%{_texmfdistdir}/tex/latex/struktex/struktex.sty
%{_texmfdistdir}/tex/latex/struktex/struktxf.sty
%{_texmfdistdir}/tex/latex/struktex/struktxp.sty
%doc %{_texmfdistdir}/doc/latex/struktex/LIESMICH
%doc %{_texmfdistdir}/doc/latex/struktex/README
%doc %{_texmfdistdir}/doc/latex/struktex/THIS_IS_VERSION_v141
%doc %{_texmfdistdir}/doc/latex/struktex/getversion.tex
%doc %{_texmfdistdir}/doc/latex/struktex/struktex-test-0.nss
%doc %{_texmfdistdir}/doc/latex/struktex/struktex-test-1.tex
%doc %{_texmfdistdir}/doc/latex/struktex/struktex-test-2.tex
%doc %{_texmfdistdir}/doc/latex/struktex/struktex-test-3.tex
%doc %{_texmfdistdir}/doc/latex/struktex/struktex-test-4.tex
%doc %{_texmfdistdir}/doc/latex/struktex/struktex.de.pdf
%doc %{_texmfdistdir}/doc/latex/struktex/struktex.el
%doc %{_texmfdistdir}/doc/latex/struktex/struktex.en.pdf
%doc %{_texmfdistdir}/doc/latex/struktex/struktex.makemake
%doc %{_texmfdistdir}/doc/latex/struktex/struktex.mk
#- source
%doc %{_texmfdistdir}/source/latex/struktex/struktex.dtx
%doc %{_texmfdistdir}/source/latex/struktex/struktex.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 141-1
+ Revision: 805082
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 133-2
+ Revision: 756255
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 133-1
+ Revision: 719595
- texlive-struktex
- texlive-struktex
- texlive-struktex
- texlive-struktex

