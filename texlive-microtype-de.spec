%global tl_name microtype-de
%global tl_revision 79121

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Translation into German of the documentation of microtype
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/obsolete/info/translations/microtype/de
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/microtype-de.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Translation into German of the documentation of microtype

