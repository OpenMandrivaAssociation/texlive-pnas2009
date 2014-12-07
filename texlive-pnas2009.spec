# revision 16287
# category Package
# catalog-ctan /biblio/bibtex/contrib/misc/pnas2009.bst
# catalog-date 2009-12-06 09:16:45 +0100
# catalog-license other-free
# catalog-version 1.0
Name:		texlive-pnas2009
Version:	1.0
Release:	9
Summary:	Bibtex style for PNAS
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/pnas2009.bst
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pnas2009.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This style produces bibliographies in the format of
"Proceedings of the National Academy of Sciences, USA". The
style was derived from the standard unsrt.bst and adapted to
the new (2009) formatting rules.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/pnas2009/pnas2009.bst

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 754984
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719279
- texlive-pnas2009
- texlive-pnas2009
- texlive-pnas2009
- texlive-pnas2009

