Name:		texlive-tikz-imagelabels
Version:	51490
Release:	2
Summary:	Put labels on images using TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikz-imagelabels
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-imagelabels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-imagelabels.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-imagelabels.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows to add label texts to an existing image
with the aid of TikZ. This may be used to label certain
features in an image.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tikz-imagelabels
%{_texmfdistdir}/tex/latex/tikz-imagelabels
%doc %{_texmfdistdir}/doc/latex/tikz-imagelabels

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
