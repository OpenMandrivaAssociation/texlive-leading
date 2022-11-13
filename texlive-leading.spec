Name:		texlive-leading
Version:	15878
Release:	1
Summary:	Define leading with a length
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leading
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leading.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leading.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leading.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command \leading, whose argument is a
<length> that specifies the nominal distance between
consecutive baselines of typeset text. The command replaces the
rather more difficult LaTeX command \linespread{<ratio>}, where
the leading is specified by reference to the font size.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/leading/leading.sty
%doc %{_texmfdistdir}/doc/latex/leading/README
%doc %{_texmfdistdir}/doc/latex/leading/leading.pdf
#- source
%doc %{_texmfdistdir}/source/latex/leading/leading.dtx
%doc %{_texmfdistdir}/source/latex/leading/leading.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
