# revision 21917
# category Package
# catalog-ctan /info/translations/microtype/de
# catalog-date 2011-04-02 10:09:07 +0200
# catalog-license lppl1.3
# catalog-version 2.4
Name:		texlive-microtype-de
Version:	2.4
Release:	1
Summary:	Translation into German of the documentation of microtype
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/microtype/de
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive microtype-de package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/microtype-de/microtype-DE.dtx
%doc %{_texmfdistdir}/doc/latex/microtype-de/microtype-DE.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
