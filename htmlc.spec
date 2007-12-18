%define name    htmlc
%define version 1.60
%define release %mkrel 4

Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        BSD like
Summary:        An HTML files generator
Group:          Publishing
URL:            http://pauillac.inria.fr/htmlc
Source:         ftp://ftp.inria.fr/INRIA/cristal/caml-light/bazar-ocaml/%{name}-%{version}.tar.bz2
patch:          %{name}-1.60.makefile.patch.bz2
BuildRequires:  ocaml
BuildRequires:  ncurses-devel

%description 
Htmlc is an HTML template files expander that produces regular HTML pages from
source files that contain text fragments that require some computation to be
written. Those fragments can be the output of an arbitrary Unix command, for
instance the last modification date of a page, or parts of HTML pages to be
included in the page, or pieces of the page that are common to the entire WEB
site (a presentation header or a footer section for each page). Providing the
automatic inclusion of those text fragments into your HTML source pages, Htmlc
offers a server independent way of defining templates to factorize out the
repetitive parts of HTML pages. Htmlc also provides a variable expansion
facility (using definitions in the template file or in simple environment files
using a syntax a la objective Caml). In short, Htmlc ensures the static
verification and the static expansion of the Server Side Includes directives of
the Web pages in the efficient and friendly way of a command-line compiler.

%prep
%setup -q
%patch -p1

%build
make \
    OCAMLC="ocamlc" \
    OCAMLOPT="ocamlopt" \
    allopt

%install
rm -rf $RPM_BUILD_ROOT
export HOST=`hostname`
make \
    BINDIR=$RPM_BUILD_ROOT%{_bindir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir} \
    installopt \
    installman
# no need for symlink
mv -f $RPM_BUILD_ROOT%{_bindir}/%{name}.bin $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Announce* INSTALL CHANGES LICENSE README
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.1*

