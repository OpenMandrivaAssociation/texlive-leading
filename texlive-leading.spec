# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/leading
# catalog-date 2008-12-15 18:32:16 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-leading
Version:	0.3
Release:	1
Summary:	Define leading with a length
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/leading
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leading.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leading.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/leading.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package defines a command \leading, whose argument is a
<length> that specifies the nominal distance between
consecutive baselines of typeset text. The command replaces the
rather more difficult LaTeX command \linespread{<ratio>}, where
the leading is specified by reference to the font size.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/leading/leading.sty
%doc %{_texmfdistdir}/doc/latex/leading/README
%doc %{_texmfdistdir}/doc/latex/leading/leading.pdf
#- source
%doc %{_texmfdistdir}/source/latex/leading/leading.dtx
%doc %{_texmfdistdir}/source/latex/leading/leading.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
