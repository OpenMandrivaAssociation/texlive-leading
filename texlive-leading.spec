# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/leading
# catalog-date 2008-12-15 18:32:16 +0100
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-leading
Version:	0.3
Release:	2
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.3-2
+ Revision: 753213
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 718840
- texlive-leading
- texlive-leading
- texlive-leading
- texlive-leading

