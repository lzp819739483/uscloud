# coding=utf-8
import libvirt
import xml.etree.cElementTree as ET
import os

hostUri = 'qemu:///system'
host = libvirt.open(hostUri)
vm_xml_path = os.path.join(os.getcwd(), 'louvm1.xml')


def createVM(vm_name, vm_cpu, vm_mem, vm_disk_path):
    status, domain = searchVM(vm_name)
    if status:
        print "%s is used" % vm_name
        return False
    try:
        vm_xml = ET.parse(vm_xml_path)
        vm_xml_root = vm_xml.getroot()
        for name in vm_xml_root.iter('name'):
            name.text = vm_name
        for vcpu in vm_xml_root.iter('vcpu'):
            vcpu.text = str(vm_cpu)
        for memory in vm_xml_root.iter('memory'):
            memory.text = str(vm_mem)
        for disk_source in vm_xml_root.iterfind('devices/disk/source'):
            disk_source.set('file', vm_disk_path)
        vm_create_path = os.path.join(os.getcwd(), vm_name+'.xml')
        vm_xml.write(vm_create_path)
        with open(vm_create_path) as f:
            domain_xml_string = f.read()
        domain = host.defineXML(domain_xml_string)
        print domain.state()
    except libvirt.libvirtError as vm_error:
        print str(vm_error)
        return False
    except Exception as exception:
        print str(exception)
        return False
    if domain.state()[0] == 5:
        return True
    else:
        return False


def shutdownVM(vm_name):
    status, domain = searchVM(vm_name)
    if not status:
        print '%s is not exits' % vm_name
        return False
    vm_state = domain.state()
    try:
        domain.destroy()
    except Exception as exception:
        return False
    if vm_state[0] == 4:
        return True
    else:
        return False


def startVM(vm_name):
    status, domain = searchVM(vm_name)
    if not status:
        print '%s is not exits' % vm_name
        return False
    try:
        domain.create()
    except Exception as exception:
        print str(exception)
        return False
    if domain.state()[0] == 1:
        return True
    else:
        return False


def getVNCPort(vm_name):
    vnc_port = None
    status, domain = searchVM(vm_name)
    if not status:
        print '%s is not exits' % vm_name
        return False
    domain_xml_str = domain.XMLDesc()
    domain_xml_root = ET.fromstring(domain_xml_str)
    for graphics in domain_xml_root.iterfind('devices/graphics'):
        vnc_port = graphics.get('port')
    return vnc_port

def rebootVM(vm_name):
    status, domain = searchVM(vm_name)
    if not status:
        print '%s is not exits' % vm_name
        return False
    try:
        if domain.state()[0] == 1:
            domain.reboot()
            return True
        else:
            return False
    except Exception as exception:
        print str(exception)
        return False

def deleteVM(vm_name):
    status, domain = searchVM(vm_name)
    if not status:
        print '%s is not exits' % vm_name
        return False
    try:
        if domain.state()[0] == 1:
            if shutdownVM(vm_name):
                domain.undefine()
                return True
            else:
                domain.undefine()
                return True
        else:
            domain.undefine()
            return True
    except Exception as exception:
        print str(exception)
        return False


def searchVM(vm_name):
    """
    根据domain名称返回一个元组，包含书否存在，domain 2个元素
    :param vm_name:
    :return:(True/False, domain/None)
    """
    domain = None
    try:
        domain = host.lookupByName(vm_name)
    except libvirt.libvirtError as vm_error:
        print str(vm_error)
        return False, domain
    except Exception as exception:
        print str(exception)
        return False, domain
    return True, domain

if __name__ == '__main__':
    # createVM('hello', 1, 512, '/home/li/workspace/louvm1.qcow2')
    # print shutdownVM('hello')
    # startVM('hello')
    # print getVNCPort('hello')
    print deleteVM('hello')
    # if searchVM('helloaa')[0]:
    #     print 'exits'
    # else:
    #     print 'no exits'
    # shutdownVM('hello')
    # startVM('hello')
    # print getVNCPort('hello')
    # rebootVM('hello')
    # delectVM('hello')