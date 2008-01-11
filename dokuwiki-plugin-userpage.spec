%define		_plugin		userpage
Summary:	DokuWiki UserPage plugin
Summary(pl.UTF-8):	Wtyczka UserPage (strony użytkowników) dla DokuWiki
Name:		dokuwiki-plugin-%{_plugin}
Version:	20070618
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://whoopdedo.org/doku-plugins/userpage.zip
# Source0-md5:	46db95c01ab4d8ad23f9648eadd15f65
URL:		http://whoopdedo.org/doku/wiki
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{_plugin}

%description
When a user registers with the wiki, this plugin will add their name
to a given page.

%description -l pl.UTF-8
Ta wtyczka dodaje do określonej strony w wiki nazwę użytkownika w
chwili jego rejestracji.

%prep
%setup -q -n %{_plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}
rm $RPM_BUILD_ROOT%{_plugindir}/{License.txt,ReadMe.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ReadMe.txt
%{_plugindir}
