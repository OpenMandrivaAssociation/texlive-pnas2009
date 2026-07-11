%global tl_name pnas2009
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	BibTeX style for PNAS (newer version)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/pnas2009.bst
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pnas2009.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This style produces bibliographies in the format of "Proceedings of the
National Academy of Sciences, USA". The style was derived from the
standard unsrt.bst and adapted to the new (2009) formatting rules.

