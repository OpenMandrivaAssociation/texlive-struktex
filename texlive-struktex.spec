Name:		texlive-struktex
Version:	75565
Release:	1
Summary:	Draw Nassi-Schneidermann charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/struktex
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/struktex
%doc %{_texmfdistdir}/doc/latex/struktex
#- source
%doc %{_texmfdistdir}/source/latex/struktex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
