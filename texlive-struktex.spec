# revision 19845
# category Package
# catalog-ctan /macros/latex/contrib/struktex
# catalog-date 2010-09-22 17:42:54 +0200
# catalog-license lppl1.2
# catalog-version 133
Name:		texlive-struktex
Version:	133
Release:	1
Summary:	Draw Nassi-Schneidermann charts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/struktex
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Even in the age of OOP one must develop algorithms. Nassi-
Shneiderman diagrams are a well known tool to describe an
algorithm in a graphical way. The package offers some macros
for generating those diagrams in a LaTeX document. The package
provides the most important elements of a Nassi-Shneiderman
diagram, including processing blocks, loops, mapping
conventions for alternatives, etc. Diagrams are drawn using the
picture environment (using pict2e for preference).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/struktex/strukdoc.sty
%{_texmfdistdir}/tex/latex/struktex/struktex.sty
%{_texmfdistdir}/tex/latex/struktex/struktxf.sty
%{_texmfdistdir}/tex/latex/struktex/struktxp.sty
%doc %{_texmfdistdir}/doc/latex/struktex/LIESMICH
%doc %{_texmfdistdir}/doc/latex/struktex/README
%doc %{_texmfdistdir}/doc/latex/struktex/THIS_IS_VERSION_v133
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
