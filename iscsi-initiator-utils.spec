%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Summary: iSCSI daemon and utility programs
Name: iscsi-initiator-utils
Version: 6.2.0.873
Release: 27%{?dist}
Source0: http://people.redhat.com/mchristi/iscsi/rhel6.0/source/open-iscsi-2.0-872-rc4-bnx2i.tar.gz
Source1: iscsid.init
Source2: iscsidevs.init
Source3: 04-iscsi

# sync iscsi tools to upstream commit 2e342633db5ac211947ffad1d8da718f6f065d3e 
# (iscsi tools: update iscsi_if.h for host event)
Patch1: iscsi-initiator-utils-sync-iscsi.patch
# Add Red Hat specific info to docs.
Patch2: iscsi-initiator-utils-update-initscripts-and-docs.patch
# Upstream uses /etc/iscsi for iscsi db info, but use /var/lib/iscsi.
Patch3: iscsi-initiator-utils-use-var-for-config.patch
# Add redhat.com string to default initiator name.
Patch4: iscsi-initiator-utils-use-red-hat-for-name.patch
# Add a lib for use by anaconda.
Patch5: iscsi-initiator-utils-add-libiscsi.patch
# Don't compile iscsistart as static
Patch7: iscsi-initiator-utils-dont-use-static.patch
# Remove the OFFLOAD_BOOT_SUPPORTED #ifdef.
Patch8: iscsi-initiator-utils-remove-the-offload-boot-supported-ifdef.patch
# fix ipv6 ibft/firmware boot
Patch9: iscsi-initiator-utils-fix-ipv6-boot.patch
# netconfig libiscsi support
Patch10: iscsi-initiator-utils-Add-Netconfig-support-through-libiscsi.patch
# libiscsi offload support
Patch11: iscsi-initiator-utils-libiscsi-to-support-offload.patch
# sync to upstream commit f9f627fbf0fc96545931ae65aa2b6214841bfd4e to
# add iscsiadm ping and host chap support and fix default iface handling
Patch12: iscsi-initiator-utils-ping-and-chap.patch 
# sync to upstream 6676a1cf6f2d23961e9db70155b5d0e5ce511989 
Patch13: iscsi-initiator-utils-mod-iface-andport-fixes.patch
# upstream Changelog, README and version sync for 2.0.873
Patch15: iscsi-initiator-utils-Prep-for-open-iscsi-2.0.873-release.patch
# upstream 71cd021b74a7094b5186a42bfe59a35e2fa66018
Patch16: iscsi-initiator-utils-iscsid-fix-iscsid-segfault-during-qla4xxx-login.patch
# upstream f0a8c95426d21413d9980d31740e193208e3280e
Patch17: iscsi-initiator-utils-ISCSISTART-Bring-up-the-corresponding-network-interf.patch
Patch18: iscsi-initiator-utils-minor-fixes-and-staying-in-synch-with-upstream-on-st.patch
Patch19: iscsi-initiator-utils-iscsiuio-0.7.8.1b.patch
Patch20: iscsi-initiator-utils-bnx2i-vlan-boot-support.patch
Patch21: iscsi-initiator-utils-Make-rescan-run-in-parallel.patch
Patch22: iscsi-initiator-utils-Fix-IDBM-errors-with-vdsm.patch
Patch23: iscsi-initiator-utils-libiscsi-fix-buffer-overflow.patch
Patch24: iscsi-initiator-utils-aligned-all-socket-comm-between-iscsiadm-iscsid-and-.patch
Patch25: iscsi-initiator-utils-flashnode-support.patch
Patch26: iscsi-initiator-utils-iscsiuio-0.7.8.2.patch
Patch27: iscsi-initiator-utils-qla-sync.patch
Patch28: iscsi-initiator-utils-sockaddr-compat.patch
Patch29: iscsi-initiator-utils-fix-handling-of-async-events.patch
Patch30: iscsi-initiator-utils-iscsiuio-revert-Fixed-a-pthread-resc-leak.patch
Patch31: iscsi-initiator-utils-initialize-param-count.patch
Patch32: iscsi-initiator-utils-iscsid-safe-session-logout.patch
Patch33: iscsi-initiator-utils-libmount-stubs-for-rhel6.patch
Patch34: iscsistart-vlan-network-setup.patch
Patch35: open-iscsi-2.0.873-117-guard-against-NULL-ptr-during-discovery-from-unexpec.patch
Patch36: open-iscsi-2.0.873-20-iscsiadm-bind-ifaces-to-portals-found-using-isns.patch
Patch37: open-iscsi-2.0.873-77-iscsid-retry-login-for-ISCSI_ERR_HOST_NOT_FOUND.patch
Patch38: open-iscsi-2.0.873-144-iscsid-make-sure-actor-is-delated-before-reschedulin.patch
Patch39: open-iscsi-2.0.873-145-iscsid-iscsiuio-remove-uio-poll.patch
Patch40: open-iscsi-2.0.873-146-iscsid-fix-iscsi_host_set_net_params-return-code.patch
Patch41: open-iscsi-2.0.873-159-iscsi_tcp-set-SO_LINGER-to-abort-connection-for-erro.patch
Patch42: open-iscsi-2.0.873-160-iscsiadm-fix-parallel-rescan-handling-of-exit-codes.patch
# 6.8 iscsiuio updates
Patch50: open-iscsi-2.0.873-80-iscsiuio-Rebranding-iscsiuio.patch
Patch51: open-iscsi-2.0.873-92-iscsiuio-Fix-warning-about-non-matching-types.patch
Patch52: open-iscsi-2.0.873-93-iscsiuio-Fix-strict-aliasing-warning-with-struct-mac.patch
Patch53: open-iscsi-2.0.873-94-iscsiuio-Resolve-strict-aliasing-issue-in-iscsiuio-s.patch
Patch54: open-iscsi-2.0.873-95-iscsiuio-Fix-aliasing-issue-with-IPV6_IS_ADDR_UNSPEC.patch
Patch55: open-iscsi-2.0.873-96-iscsiuio-Use-attribute-unused-for-variables-that-are.patch
Patch56: open-iscsi-2.0.873-97-iscsiuio-Use-attribute-unused-for-icmpv6_hdr.patch
Patch57: open-iscsi-2.0.873-98-iscsiuio-Change-nic_disable-to-return-void.patch
Patch58: open-iscsi-2.0.873-99-iscsiuio-Remove-set-but-unused-variables.patch
Patch59: open-iscsi-2.0.873-100-iscsiuio-Check-return-value-from-nic_queue_tx_packet.patch
Patch60: open-iscsi-2.0.873-120-iscsiuio-CFLAGS-fixes.patch
Patch61: open-iscsi-2.0.873-135-iscsiuio-Correct-the-handling-of-Multi-Function-mode.patch
Patch62: open-iscsi-2.0.873-137-ARP-table-too-small-when-switches-involved.patch
Patch63: open-iscsi-libiscsi-vlan-id.patch
Patch64: open-iscsi-2.0.873-138-use-24-bits-of-ISID-qualifier-space-instead-of-only-.patch
Patch65: open-iscsi-2.0.873-157-remove-sysfs-attr_list.patch
Patch66: open-iscsi-2.0.873-148-iscsid-Changes-to-support-ping-through-iscsiuio.patch
Patch67: open-iscsi-2.0.873-149-iscsiuio-Add-ping-support-through-iscsiuio.patch
Patch68: open-iscsi-2.0.873-150-iscsiadm-let-ping-be-tried-after-iface-config-is-ini.patch
Patch69: open-iscsi-2.0.873-151-iscsiuio-Wait-for-iface-to-be-ready-before-issuing-t.patch
Patch70: open-iscsi-2.0.873-152-iscsiuio-Get-the-library-to-use-based-on-uio-sysfs-n.patch
Patch71: open-iscsi-2.0.873-iscsiuio-autoreconf.patch
Patch72: open-iscsi-2.0.873-70-iscsi-tools-set-non-negotiated-params-early.patch
# 6.9 iscsiuio updates
Patch80: open-iscsi-2.0.873-147-iscsiuio-Add-QLogic-Vendor-ID-to-support-newer-NX2-H.patch
Patch81: open-iscsi-2.0.873-153-iscsiuio-Do-not-memcpy-identical-locations.patch
Patch82: open-iscsi-2.0.873-154-iscsiuio-Clear-memory-after-allocation.patch
Patch83: open-iscsi-2.0.873-155-iscsiuio-fixup-race-condition.patch
Patch84: open-iscsi-2.0.873-157-Prevent-iscsiuio-from-segfaulting-due-to-un-lock-of-.patch
Patch85: open-iscsi-2.0.873-158-iscsiuio-ensure-unlock-of-mutex-in-case-of-an-error.patch
Patch86: open-iscsi-fix-regression-in-iscsi_tcp-iface-binding.patch
# add rhel version info to iscsi tools
Patch90: iscsi-initiator-utils-add-rh-ver.patch

Group: System Environment/Daemons
License: GPLv2+
URL: http://www.open-iscsi.org
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: flex bison python-devel doxygen kernel-headers

Requires(post): chkconfig
Requires(preun): chkconfig /sbin/service

%description
The iscsi package provides the server daemon for the iSCSI protocol,
as well as the utility programs used to manage it. iSCSI is a protocol
for distributed disk access using SCSI commands sent over Internet
Protocol networks.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n open-iscsi-2.0-872-rc4-bnx2i
%patch1 -p1 -b .sync-iscsi
%patch2 -p1 -b .update-initscripts-and-docs
%patch3 -p1 -b .use-var-for-config
%patch4 -p1 -b .use-red-hat-for-name
%patch5 -p1 -b .add-libiscsi
%patch7 -p1 -b .dont-use-static
%patch8 -p1 -b .remove-the-offload-boot-supported-ifdef
%patch9 -p1 -b .fix-ipv6-boot
%patch10 -p1 -b .Add-Netconfig-support-through-libiscsi
%patch11 -p1 -b .libiscsi-to-support-offload
%patch12 -p1 -b .ping-and-chap
%patch13 -p1 -b .mod-iface-andport-fixes
%patch15 -p1 -b .sync-2.0.873
%patch16 -p1 -b .segfault-qla4xxx-login
%patch17 -p1 -b .boot-netif-up
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1 -b .iscsiuio-0.7.8.2
%patch27 -p1 -b .qla-sync
%patch28 -p1 -b .sockaddr
%patch29 -p1 -b .async-events
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch90 -p1 -b .add-rh-ver

%build
cd utils/open-isns
./configure --with-security=no --with-slp=no
make OPTFLAGS="%{optflags}"
cd ../../
make OPTFLAGS="%{optflags}" -C utils/sysdeps
make OPTFLAGS="%{optflags}" -C utils/fwparam_ibft
make OPTFLAGS="%{optflags}" -C usr
make OPTFLAGS="%{optflags}" -C utils
make OPTFLAGS="%{optflags}" -C libiscsi

cd iscsiuio
chmod u+x configure
./configure --enable-debug
make OPTFLAGS="%{optflags}"
cd ..

pushd libiscsi
python setup.py build
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
mkdir -p $RPM_BUILD_ROOT/etc/iscsi
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d
mkdir -p $RPM_BUILD_ROOT/etc/NetworkManager/dispatcher.d
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi/nodes
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi/send_targets
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi/static
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi/isns
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi/slp
mkdir -p $RPM_BUILD_ROOT/var/lib/iscsi/ifaces
mkdir -p $RPM_BUILD_ROOT/var/lock/iscsi
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}
mkdir -p $RPM_BUILD_ROOT%{python_sitearch}



install -p -m 755 usr/iscsid usr/iscsiadm utils/iscsi-iname usr/iscsistart $RPM_BUILD_ROOT/sbin
install -m 755 iscsiuio/src/unix/iscsiuio $RPM_BUILD_ROOT/sbin
install -p -m 644 doc/iscsiadm.8 $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 doc/iscsid.8 $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 doc/iscsistart.8 $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 doc/iscsi-iname.8 $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 iscsiuio/docs/iscsiuio.8 $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 iscsiuio/iscsiuiolog $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -p -m 644 etc/iscsid.conf $RPM_BUILD_ROOT%{_sysconfdir}/iscsi

install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_initrddir}/iscsid
install -p -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/iscsi
install -p -m 755 %{SOURCE3} $RPM_BUILD_ROOT/etc/NetworkManager/dispatcher.d

install -p -m 755 libiscsi/libiscsi.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libiscsi.so.0 $RPM_BUILD_ROOT%{_libdir}/libiscsi.so
install -p -m 644 libiscsi/libiscsi.h $RPM_BUILD_ROOT%{_includedir}

install -p -m 755 libiscsi/build/lib.linux-*/libiscsimodule.so \
	$RPM_BUILD_ROOT%{python_sitearch}
#compat support for older tools that are not aware of the name change
ln -s iscsiuio $RPM_BUILD_ROOT/sbin/brcm_iscsiuio


%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

if [ "$1" -eq "1" ]; then
	if [ ! -f %{_sysconfdir}/iscsi/initiatorname.iscsi ]; then
		echo "InitiatorName=`/sbin/iscsi-iname`" > %{_sysconfdir}/iscsi/initiatorname.iscsi
	fi
	/sbin/chkconfig --add iscsid
	/sbin/chkconfig --add iscsi
fi

%postun -p /sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	# stop iscsi
	/sbin/service iscsi stop > /dev/null 2>&1
	# delete service
	/sbin/chkconfig --del iscsi
	# stop iscsid
	/sbin/service iscsid stop > /dev/null 2>&1
	# delete service
	/sbin/chkconfig --del iscsid
fi

%files
%defattr(-,root,root)
%doc README
%dir /etc/iscsi
%dir %{_var}/lib/iscsi
%dir %{_var}/lib/iscsi/nodes
%dir %{_var}/lib/iscsi/isns
%dir %{_var}/lib/iscsi/static
%dir %{_var}/lib/iscsi/slp
%dir %{_var}/lib/iscsi/ifaces
%dir %{_var}/lib/iscsi/send_targets
%dir %{_var}/lock/iscsi
%{_initrddir}/iscsi
%{_initrddir}/iscsid
%{_sysconfdir}/NetworkManager
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/iscsi/iscsid.conf
/sbin/*
%{_libdir}/libiscsi.so.0
%{python_sitearch}/libiscsimodule.so
%{_mandir}/man8/*
%config(noreplace) /etc/logrotate.d/iscsiuiolog

%files devel
%defattr(-,root,root,-)
%doc libiscsi/html
%{_libdir}/libiscsi.so
%{_includedir}/libiscsi.h

%changelog
* Wed Jun 07 2017 Chris Leech <cleech@redhat.com> - 6.2.0.873-27
- 1170750 apply "Set non negotiated params early" from upstream
  to fix SendTargets discovery over iSER with some targets

* Mon Jan 09 2017 Chris Leech <cleech@redhat.com> - 6.2.0.873-26
- 1400844 regression in interface binding

* Thu Oct 13 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-25
- 1380316 iscsiuio updates

* Wed Oct 12 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-24
- 1121670 iscsid enter infinite loop if conn_bind fails

* Wed Oct 12 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-23
- 1215578 iscsiadm rescan fails in node mode
- 1311818 data corruption during ethernet port failure

* Mon Aug 08 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-22
- 1004015 fix binding of iSNS discovered targets to ifaces

* Mon Mar 28 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-21
- 1294965 iscsiuio match based on driver to support new hardware without
  adding PCI IDs (still need IDs added to kernel)
- bnx2i pass through ping support

* Thu Mar 10 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-20
- 1314926 return NULL for no attr instead of an empty string

* Mon Feb 29 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-19
- 1309724 fix regression in ibft sysfs reading

* Wed Feb 17 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-18
- remove sysfs att_list cache, speed up handling of large number of sessions

* Fri Jan 29 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-17
- use 24-bits of ISID space

* Wed Jan 20 2016 Chris Leech <cleech@redhat.com> - 6.2.0.873-16
- 831002 added vlan id to libiscsi reported network configuration

* Fri Dec 11 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-15
- 1125984 iscsistart vlan support
- 906242 fix segfault from unexpected netlink event during driver load
- 1181463 iscsiuio update

* Thu Feb 26 2015 Chris Leech <cleech@redhat.com> - 6.2.0.873-14
- 691746 add safe logout mode to block session logout when devices are mounted

* Tue Sep 09 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-13
- 1053374 fix uninitialized param_count variable

* Fri Sep 05 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-12
- 1132490 iscsiuio terminates with segfault or sigabrt

* Thu Jun 19 2014 Chris Leech <cleech@redhat.com> - 6.2.0.873-11
- 1054587 iscsiuio update
- 1053374 upstream backports to support new driver features
- 1052361 IPC sockaddr compat to communicate with older iscsid on upgrade
- 1076344 fix handling of multiple oustanding async events

* Tue Oct 08 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-10
- 884427 update fix to remove dead discovery links

* Fri Sep 20 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-9
- 917600 add flash node managment support

* Fri Sep 06 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-8
- fix communications issue between iscsid and iscsiuio

* Tue Aug 27 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-7
- 1001705 regression caused by fix for 884427 in 6.2.0.873-3

* Fri Aug 23 2013 Andy Grover <agrover@redhat.com> - 6.2.0.873-6
- Update bnx2i-vlan-boot-support.patch to check session != NULL
  before calling iscsi_sysfs_read_iface

* Wed Aug 14 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-5
- fix buffer overflow warning regression in libiscsi

* Tue Aug 13 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-4
- fix buffer overflow warning regression in libiscsi

* Tue Aug 13 2013 Chris Leech <cleech@redhat.com> - 6.2.0.873-3
- 831003 boot over VLAN support patches
- 916007 replace iscsiuio with code merged upstream 0.7.8.1b
- 884427 fix for db errors when vdsm creates static entries for
         target portals already setup through discovery
- 983553 run target refresh in parallel so unreachable doesn't block others

* Mon Oct 22 2012 Chris Leech <cleech@redhat.com> - 6.2.0.873-2
- 868305 sync iscsiuio to 0.7.6.1

* Thu Oct 11 2012 Chris Leech <cleech@redhat.com> - 6.2.0.873-1
- Sync with upstream 2.0.873
- 854776 Bring up network interface for iSCSI boot with bnx2i
- 811428 make version string reported by iscsiadm match RPM version
- fix iscsid segfault during qla4xxx login

* Wed Oct 10 2012 Chris Leech <cleech@redhat.com> - 6.2.0.872-42
- 826300 sync iscsiuio to 0.7.4.3

* Thu Apr 5 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.41
- 810197 Coverity fixes.
- 740054 fix iscsiuio version string

* Wed Apr 4 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.40
- 738192 Fix regression added when handling 738192 where unknown params
  messages got logged by mistake.

* Wed Mar 28 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.39
- 738192 Fix invalid param handling.
- 790609 Fix --interval iscsiadm handling. 

* Thu Mar 22 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.38
- Fix regressions caused by 796574 and 805467.

* Thu Mar 22 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.37
- 805467 Have iscsistart/iscsiadm bring up offload net interface.
- 796574 Fix port handling when hostnames are used for portals.
- 739843 Fix default iface setup handling.

* Mon Mar 5 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.36
- 740054 sync iscsiuio to 0.7.2.1
- 790609 Add ping and host chap support to iscsiadm
- 636013 scalability testing.

* Sun Feb 26 2012 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.35
- 738192 Allow iscsistart to take any parameter.
- 739049 Fix -i use in README.

* Tue Nov 1 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.34
- 750714 Do not build with SLP.

* Tue Nov 1 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.33
- 749051 More offload boot fixups.

* Tue Oct 25 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.31
- 749051 Sync iscsiuio to iscsiuio-0.7.0.14g to fix boot hang
  when connection is lost during startup.

* Tue Oct 18 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.30
- 602959 rotate iscsiuio/brcm_iscsiuio log.

* Tue Oct 11 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.28
- 736116 (again) fix aligment for iface nl msgs.
- Fix iscsid restart issue when using qla4xxx boot.
- Fix ipv6 boot when using ibft.

* Thu Sep 20 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.27
- 736116 Fix netlink msg len

* Thu Sep 8 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.26
- Fix offload removal patch

* Thu Sep 1 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.25
- 732912 Fix return value/msg when iscsiadm fails to log into target
- 696808 Update iscsiuio to v0.7.0.14.

* Sun Aug 14 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.24
- 696808 Fix brcm_iscsiuio naming from change in 696808

* Sun Aug 14 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.23
- 696808 Sync brcm/uio to v0.7.0.8.
- 715434 Fix iscsiadm command line help discoverydb/discovery2 description.

* Tue Apr 19 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.21
- 593269 iscsi was built against libcrypto, but was not using the code
so this disabled the building of that code [patch from .14 got dropped
due to mismerge].

* Mon Apr 18 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.20
- 696267 Create a offloaded session if the iscsi_host MAC and ibft
MAC match. This enables support for Broadcoms hba boot mode.

* Tue Apr 5 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.19
- 624437 support hostnames in node mode. [patch merged in .14 got
 dropped by accident]

* Thu Feb 24 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.18
- fix iscsiadm exit code when iscsid is not running and the
discovery command is run.
- 689359 Fix uIP when using DCB for FCoE
- 691902 Fix iscsiadm SendTargets offload support when the PDU's data len
is 8K. 

* Sat Feb 19 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.17
- 634021 Fix in .14 added regression during iscsi startup that prevented
sessions from getting created.

* Wed Feb 9 2011 Ales Kozumplik <akozumpl@redhat.com> 6.2.0.872.16
- 529443 fwparam_sysfs: fix pathname manipulation error in
  fwparam_sysfs_boot_info.
- 529443 Make libiscsi nodes remember the interface they connect through.

* Thu Feb 3 2011 Mike Christie <mcrhsit@redhat.com> 6.2.0.872.15
- 640340 fix iscsiadm exit codes.
- 523492 iSCSI DCB support

* Mon Jan 31 2011 Mike Christie <mchristi@redhat.com> 6.2.0.872.14
- 593269 iscsi was built against libcrypto, but was not using the code
so this disabled the building of that code.
- 599539 document brcm_iscsiuio options in man page.
- 599542 document iscsiadm host mode hostno argument.
- 631821 iscsi discovery was not incrementing ITT when multiple text
commands were sent. This prevented discovery from finding all targets.
- 634021 iscsi init script did not shutdown all sessions during system
shutdown/reboot causing the host to hang.
- 658428 iscsi init script should not shutdown sessions when root is
using them and should not fail startup on all iscsiadm login failures.
- 635899 sync brcm_iscsiuio to 0.6.2.13 to add support for IPv6, VLAN,
57711E, and 57712 hardware.
- 640115 fix hang caused due to race in ISCSI_ERR_INVALID_HOST handling.
- 640340 fix iscsiadm exit codes.
- 624437 support hostnames in node mode.

* Fri Dec 3 2010 Ales Kozumplik <akozumpl@redhat.com> 6.2.0.872.13
- 442980 libiscsi: reimplement fw discovery so partial devices are used properly.

* Tue Nov 30 2010 Ales Kozumplik <akozumpl@redhat.com> 6.2.0.872.12
- 442980 partial offload boot: Remove the OFFLOAD_BOOT_SUPPORTED ifdef. This
  effectively makes OFFLOAD_BOOT_SUPPORTED always enabled.

* Mon Nov 29 2010 Ales Kozumplik <akozumpl@redhat.com> 6.2.0.872.11
- 442980 brcm uio: handle the different iface_rec structures in iscsid and brcm.

* Wed Aug 18 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.10
- 605663 Log message when iface binding, and doc rp_filter settings
  needed for iface binding.

p* Mon Aug 5 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.9
- 614035 Make iscsi status print session info.
- Fix uip vlan and 10 gig bugs.

* Mon Jul 26 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.8
- 589256 Re-fix iface update/delete return value.

* Mon Jul 12 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.7
- 595591 Fix nic state bug in brcm_iscsiuio.

* Thu Jul 8 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.6
- 602899 Add discovery db support.
- 595591 Sync brcm_iscsiuio to 0.5.15.
- 589256 Do not log success message and return ENODEV
- 601434 Fix iscsiadm handling of non-default port

* Fri Jun 18 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.5
- 602286 No need to compile iscsistart as static. This also fixes
  the segfault when hostnames are passed in for the portal ip.

* Tue May 18 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.4
- 590580 libiscsi get_firmware_foo does not work without first creating a
  libiscsi context
- 588931 Fix uip and iscsid initialization race
- 570664 Add basic vlan support for bnx2i's brcm uip daemon
- 589761 Fix multiple init script bugs: rh_status does not detect offload,
  start/stop does not work due to iscsiadm output being directed to stderr,
  discovery daemon does not get auto started/stopped, iscsid restart does
  not restart daemon if force-start was used.
- 585649 Fix iscsid "-eq: unary operator expected" bug.

* Wed May 5 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.3
- 578455 Fix initial R2T=0 handling for be2iscsi

* Wed Mar 31 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.2
- 578455 Fix handling of MaxXmitDataSegmentLength=0 for be2iscsi

* Wed Mar 31 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.1
- 578455 Fix handling of MaxXmitDataSegmentLength=0

* Wed Mar 24 2010 Mike Christie <mchristi@redhat.com> 6.2.0.872.0
- 516444 Add iSNS SCN handling (rebased to open-iscsi-2.0-872-rc1-)
- Update brcm to 0.5.7

* Mon Feb 8 2010 Mike Christie <mchristi@redhat.com> 6.2.0.871.1.1-3
- Add spec patch comments.

* Thu Jan 21 2010 Mike Christie <mchristi@redhat.com> 6.2.0.871.1.1-2
- 556985 Fix up init.d iscsid script to remove offload modules and
  load be2iscsi.
- Enable s390/s390x

* Fri Jan 15 2010 Mike Christie <mchristi@redhat.com> 6.2.0.871.1.1-1
- Sync to upstream
- 529324 Add iscsi-iname and iscsistart man page
- 463582 OF/iBFT support

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.870-10.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Dan Horak <dan[at]danny.cz> 6.2.0.870-9.1
- drop the s390/s390x ExcludeArch

* Mon Apr 27 2009 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-9
- Don't crash when asked to parse the ppc firmware table more then
  once (which can be done from libiscsi) (#491363)

* Fri Apr  3 2009 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-8
- Stop the NM script from exiting with an error status when it
  didn't do anything (#493411)

* Fri Mar 20 2009 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-7
- libiscsi: use fwparam_ibft_sysfs() instead of fw_get_entry(), as
  the latter causes stack corruption (workaround #490515)

* Sat Mar 14 2009 Terje Rosten <terje.rosten@ntnu.no> - 6.2.0.870-6
- Add glibc-static to buildreq to build in F11

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0.870-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-4
- Fix libiscsi.discover_sendtargets python method to accept None as valid
  authinfo argument (#485217)

* Wed Jan 28 2009 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-3
- Fix reading of iBFT firmware with newer kernels

* Wed Jan 28 2009 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-2
- Add libiscsi iscsi administration library and -devel subpackage

* Tue Nov  25 2008 Mike Christie <mchristie@redhat.com> 6.2.0.870-1.0
- Rebase to upstream

* Thu Nov  6 2008 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-0.2.rc1
- Add force-start iscsid initscript option and use that in "patch to make
  iscsiadm start iscsid when needed" so that iscsid will actual be started
  even if there are no iscsi disks configured yet (rh 470437)
- Do not start iscsid when not running when iscsiadm -k 0 gets executed
  (rh 470438)

* Tue Sep 30 2008 Hans de Goede <hdegoede@redhat.com> 6.2.0.870-0.1.rc1
- Rewrite SysV initscripts, fixes rh 441290, 246960, 282001, 436175, 430791
- Add patch to make iscsiadm complain and exit when run as user instead
  of hang spinning for the database lock
- Add patch to make iscsiadm start iscsid when needed (rh 436175 related)
- Don't start iscsi service when network not yet up (in case of using NM)
  add NM dispatcher script to start iscsi service once network is up

* Mon Jun 30 2008 Mike Christie <mchristie@redhat.com> - 6.2.0.870
- Rebase to open-iscsi-2-870
- 453282 Handle sysfs changes.

* Fri Apr 25 2008 Mike Christie <mchristie@redhat.com> - 6.2.0.868-0.7
- 437522 log out sessions that are not used for root during "iscsi stop".

* Fri Apr 4 2008 Mike Christie <mchristie@redhat.com> - 6.2.0.868-0.6
- Rebase to RHEL5 to bring in bug fixes.
- 437522 iscsi startup does not need to modify with network startup.
- 436175 Check for running sessions when stopping service.

* Wed Feb 5 2008 Mike Christie <mchristie@redhat.com> - 6.2.0.868-0.3
- Rebase to upstream and RHEL5.
- 246960 LSB init script changes.

* Fri Oct 5 2007 Mike Christie <mchristie@redhat.com> - 6.2.0.865-0.2
- Rebase to upstream's bug fix release.
- Revert init script startup changes from 225915 which reviewers did
 not like.

* Mon Jun 20 2007 Mike Christie <mchristie@redhat.com> - 6.2.0.754-0.1
- 225915 From Adrian Reber - Fix up spec and init files for rpmlint.

* Tue Feb 6 2007 Mike Christie <mchristie@redhat.com> - 6.2.0.754-0.0
- Rebase to upstream.
- Add back --map functionality but in session mode to match RHEL5 fixes
- Break up iscsi init script into two, so iscsid can be started early for root

* Tue Nov 28 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.747-0.0
- Fix several bugs in actor.c (iscsi scheduling). This should result
- in better dm-multipath intergation and fix bugs where time outs
- or requests were missed or dropped.
- Set default noop timeout correctly.

* Sat Nov 25 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.742-0.0
- Don't flood targets with nop-outs.

* Fri Nov 24 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.737-0.0
- Add commands missing from RHEL4/RHEL3 and document iscsid.conf.
- Fixup README.

* Mon Nov 7 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.8
- Rebase to upstream open-iscsi-2.0-730.

* Tue Oct 17 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.7
- Change period to colon in default name

* Thu Oct 5 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.6
- BZ 209523 make sure the network is not going to get shutdown so
iscsi devices (include iscsi root and dm/md over iscsi) get syncd.
- BZ 209415 have package create iscsi var dirs

* Tue Oct 3 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.5
- BZ 208864 move /etc/iscsi/nodes and send_targets to /var/lib/iscsi

* Mon Oct 1 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.4
- BZ 208548 move /etc/iscsi/lock to /var/lock/iscsi/lock

* Wed Sep 27 2006 Jeremy Katz <katzj@redhat.com> - 6.2.0.695-0.3
- Add fix for initscript with pid file moved

* Tue Sep 26 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.2
- BZ 208050 - change default initiator name to reflect redhat
- Move pid from /etc/iscsi to /var/run/iscsid.pid

* Fri Sep 15 2006 Mike Christie <mchristie@redhat.com> - 6.2.0.695-0.1
- Add compat with FC kernel so iscsid will pass startup checks and run.
- Fix bug when using hw iscsi and software iscsi and iscsid is restarted.
- Fix session matching bug when hw and software iscsi is both running

* Tue Sep  5 2006 Jeremy Katz <katzj@redhat.com> - 6.1.1.685-0.1
- Fix service startup
- Fix another case where cflags weren't being used

* Mon Aug 28 2006 Mike Christie <mchristie@redhat.com> - 6.1.1.685
- Rebase to upstream to bring in many bug fixes and rm db.
- iscsi uses /etc/iscsi instead of just etc now

* Fri Jul 21 2006 Jeremy Katz <katzj@redhat.com> - 6.1.1.645-1
- fix shutdown with root on iscsi

* Thu Jul 13 2006 Mike Christie <mchristie@redhat.com> - 6.1.1.645
- update to upstream 1.1.645
- Note DB and interface changed so you must update kernel, tools and DB

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.0.5.595-2.1.1
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 6.0.5.595-2.1
- rebuild

* Wed Jun 21 2006 Mike Christie <mchristi@redhat.com> - 6.0.5.595-2
- add PatM's statics.c file. This is needed for boot since 
  there is no getpwuid static available at that time.
* Tue Jun 20 2006 Jeremy Katz <katzj@redhat.com> - 6.0.5.595-1
- ensure that we respect %%{optflags}
- cleaned up initscript to make use of standard functions, return right 
  values and start by default
- build iscsistart as a static binary for use in initrds

* Tue May 30 2006 Mike Christie <mchristi@redhat.com>
- rebase package to svn rev 595 to fix several bugs
  NOTE!!!!!!!! This is not compatible with the older open-iscsi modules
  and tools. You must upgrade.

* Thu May 18 2006 Mike Christie <mchristi@redhat.com>
- update package to open-iscsi svn rev 571
  NOTE!!!!!!!! This is not compatible with the older open-iscsi modules
  and tools. You must upgrade.

* Fri Apr 7 2006 Mike Christie <mchristi@redhat.com>
- From Andy Henson <andy@zexia.co.uk>:
  Autogenerate /etc/initiatorname.iscsi during install if not already present
- Remove code to autogenerate /etc/initiatorname.iscsi from initscript
- From dan.y.roche@gmail.com:
  add touch and rm lock code
- update README
- update default iscsid.conf. "cnx" was not supported. The correct
  id was "conn".

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 5.0.5.476-0.1
- bump again for double-long bug on ppc(64)

* Mon Jan 23 2006 Mike Christie <mchristi@redhat.com>
- rebase package to bring in ppc64 unsigned long vs unsigned
  long long fix and iscsadm return value fix. Also drop rdma patch
  becuase it is now upstream.
* Wed Dec 14 2005 Mike Christie <mchristi@redhat.com>
- initial packaging

