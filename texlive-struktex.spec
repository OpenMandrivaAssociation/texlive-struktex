%global tl_name struktex
%global tl_revision 75565

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0a
Release:	%{tl_revision}.1
Summary:	Draw Nassi-Shneiderman charts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/struktex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/struktex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Even in the age of OOP one must develop algorithms. Nassi-Shneiderman
charts are a well known tool to describe an algorithm in a graphical
way. The package offers some macros for generating those charts in a
LaTeX document. The package provides the most important elements of a
Nassi-Shneiderman charts, including processing blocks, loops, mapping
conventions for alternatives, etc. The charts are drawn using the
picture environment (using pict2e for preference).

