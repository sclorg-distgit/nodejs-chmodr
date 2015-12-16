%{?scl:%scl_package nodejs-chmodr}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-chmodr
Version:    0.1.0
Release:    4.sc1%{?dist}
Summary:    Recursively change UNIX file permissions
License:    BSD
Group:      System Environment/Libraries
URL:        https://github.com/isaacs/chmodr
Source0:    http://registry.npmjs.org/chmodr/-/chmodr-%{version}.tgz
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%description
%{summary}, like `chmod -R`.

%prep
%setup -q -n package

%build
#nothing to do

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{nodejs_sitelib}/chmodr
cp -pr chmodr.js package.json %{buildroot}%{nodejs_sitelib}/chmodr

%nodejs_symlink_deps

# disabled; TAP is not in the distro yet
#%%check
#%%tap test/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{nodejs_sitelib}/chmodr
%doc README.md LICENSE

%changelog
* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-4
- replace provides and requires with macro

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1.0-3
- Add support for software collections

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-2
- fix License tag

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- initial package
