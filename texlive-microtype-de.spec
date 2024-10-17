Name:		texlive-microtype-de
Version:	54080
Release:	2
Summary:	Translation into German of the documentation of microtype
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/microtype/de
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
