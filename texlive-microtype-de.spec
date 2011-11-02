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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
