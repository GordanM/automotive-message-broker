Name:       automotive-message-broker
Summary:    Automotive Message Broker is a vehicle network abstraction system.
Version:    0.1
Release:    1
Group:      System/Base
License:    LGPL v2.1
URL:        https://github.com/otcshare/automotive-message-broker
Source0:    %{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  json-glib-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libwebsockets-devel

%description
Automotive Message Broker is a vehicle network abstraction system.
It brokers information from the vehicle to applications.

%package devel
Summary:    automoive-message-broker development files
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for the automotive-message-broker

%package doc
Summary:    Documentation for the API
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description doc
Document files that describe the D-Bus API exposed by automotive-message-broker

%package plugins
Summary:    Various plugins for automotive-message-broker
Group:      System/Base
Requires:   %{name} = %{version}-%{release}

%description plugins
Collection of plugins for automotive-message-broker

%prep
%setup -q -n %{name}-%{version}

%build
%cmake

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post plugins -p /sbin/ldconfig
%postun plugins -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/ambd/config
%{_bindir}/*
%{_libdir}/libamb.so*
%{_libdir}/systemd/system/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libamb.so*
%{_includedir}/amb/*.h
%{_libdir}/pkgconfig/*.pc

%files plugins
%defattr(-,root,root,-)
%{_libdir}/%{name}/*.so

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/*.txt