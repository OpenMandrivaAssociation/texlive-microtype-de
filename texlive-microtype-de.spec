# revision 24549
# category Package
# catalog-ctan /info/translations/microtype/de
# catalog-date 2011-04-03 23:29:51 +0200
# catalog-license lppl1.3
# catalog-version 2.4
Name:		texlive-microtype-de
Version:	2.4
Release:	13
Summary:	Translation into German of the documentation of microtype
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/microtype/de
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive microtype-de package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/microtype-de/microtype-DE.dtx
%doc %{_texmfdistdir}/doc/latex/microtype-de/microtype-DE.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.4-3
+ Revision: 753982
- Rebuild to reduce used resources

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4-2
+ Revision: 729682
- texlive-microtype-de

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.4-1
+ Revision: 719024
- texlive-microtype-de
- texlive-microtype-de
- texlive-microtype-de
- texlive-microtype-de

